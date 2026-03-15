// ── Photo preview ──────────────────────────────────────────────────────────
function previewPhoto(input) {
  const file = input.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(e) {
    document.getElementById('photo-preview').src = e.target.result;
    document.getElementById('photo-preview-wrap').style.display = 'block';
  };
  reader.readAsDataURL(file);
}

function removePhoto() {
  document.getElementById('photo-preview').src = '';
  document.getElementById('photo-preview-wrap').style.display = 'none';
  document.getElementById('photo-input').value = '';
}

// ── Like buttons ──────────────────────────────────────────────────────────
document.querySelectorAll('.like-btn').forEach(btn => {
  btn.addEventListener('click', async () => {
    const id = btn.dataset.id;
    const svg = btn.querySelector('svg');
    const span = btn.querySelector('span');
    if (btn.classList.contains('liked')) {
      btn.classList.remove('liked');
      svg.setAttribute('fill', 'none');
      svg.setAttribute('stroke', 'currentColor');
      span.textContent = 'Like';
      span.style.color = '';
    } else {
      btn.classList.add('liked');
      svg.setAttribute('fill', 'var(--rd)');
      svg.setAttribute('stroke', 'var(--rd)');
      span.textContent = 'Liked';
      span.style.color = 'var(--rd)';
      try { await fetch(`/api/like/${id}`, { method: 'POST' }); } catch(e) {}
    }
  });
});

// ── New post submit ────────────────────────────────────────────────────────
const submitBtn = document.getElementById('submit-post');
if (submitBtn) {
  submitBtn.addEventListener('click', async () => {
    const input = document.getElementById('post-input');
    const content = input.value.trim();
    const photoPreview = document.getElementById('photo-preview');
    const photoSrc = photoPreview ? photoPreview.src : '';
    const hasPhoto = photoSrc && photoSrc.startsWith('data:');

    if (!content && !hasPhoto) { alert('Kuch likhein ya photo chunein!'); return; }

    try {
      const res = await fetch('/api/post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content, photo: hasPhoto ? photoSrc : null }),
      });
      const data = await res.json();
      if (data.ok) {
        const container = document.getElementById('posts-container');
        const div = document.createElement('div');
        div.className = 'post';
        div.dataset.id = data.post.id;
        const lid = 'nlk' + data.post.id;
        const cid = 'nlc' + data.post.id;
        div.innerHTML = `
          <div class="post-head">
            <div class="post-av">😊</div>
            <div style="flex:1">
              <div class="post-name">Aap (You)</div>
              <div class="post-time">Abhi · Meerut, UP</div>
            </div>
          </div>
          ${content ? `<div class="post-body">${content.replace(/</g,'&lt;').replace(/\n/g,'<br>').replace(/#(\w+)/g,'<span style="color:var(--ac)">#$1</span>')}</div>` : ''}
          ${hasPhoto ? `<div class="post-thumb-wrap"><img class="post-thumb" src="${photoSrc}" alt="Post photo"><div class="post-img-label">Aapki Photo</div></div>` : ''}
          <div class="post-stats">0 likes · 0 comments · 0 shares</div>
          <div class="post-actions">
            <div class="pact like-btn" id="${lid}" data-id="${data.post.id}">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
              </svg>
              <span id="${cid}">Like</span>
            </div>
            <div class="pact"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>Comment</div>
            <div class="pact"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>Share</div>
          </div>`;

        // attach like handler
        div.querySelector('.like-btn').addEventListener('click', function() {
          const s = this.querySelector('svg'), sp = this.querySelector('span');
          if (this.classList.contains('liked')) {
            this.classList.remove('liked'); s.setAttribute('fill','none'); s.setAttribute('stroke','currentColor');
            sp.textContent='Like'; sp.style.color='';
          } else {
            this.classList.add('liked'); s.setAttribute('fill','var(--rd)'); s.setAttribute('stroke','var(--rd)');
            sp.textContent='Liked'; sp.style.color='var(--rd)';
          }
        });

        container.insertBefore(div, container.firstChild);
        input.value = '';
        removePhoto();
      }
    } catch(e) { alert('Post nahi ho saka. Dobara try karo!'); }
  });
}

// ── Sale countdown timer ───────────────────────────────────────────────────
const timerEl = document.getElementById('sale-timer');
if (timerEl) {
  let sec = 51827;
  setInterval(() => {
    sec = sec > 0 ? sec - 1 : 86400;
    const h = Math.floor(sec / 3600).toString().padStart(2,'0');
    const m = Math.floor((sec % 3600) / 60).toString().padStart(2,'0');
    const s = (sec % 60).toString().padStart(2,'0');
    timerEl.textContent = `Ends in: ${h}:${m}:${s}`;
  }, 1000);
}

// ── Tab bar ────────────────────────────────────────────────────────────────
document.querySelectorAll('.tb').forEach(tb => {
  tb.addEventListener('click', function() {
    this.closest('.tab-bar').querySelectorAll('.tb').forEach(x => x.classList.remove('on'));
    this.classList.add('on');
  });
});

// ── Category pills ─────────────────────────────────────────────────────────
document.querySelectorAll('.cp').forEach(cp => {
  cp.addEventListener('click', function() {
    this.closest('.cpill').querySelectorAll('.cp').forEach(x => x.classList.remove('on'));
    this.classList.add('on');
  });
});

// ── Live Stock Prices ──────────────────────────────────────────────────────
async function loadStocks() {
  try {
    const res = await fetch('/api/stocks');
    const data = await res.json();
    for (const [name, val] of Object.entries(data)) {
      if (!val) continue;
      const priceEl = document.getElementById('s-' + name);
      const chgEl   = document.getElementById('c-' + name);
      if (priceEl) priceEl.textContent = val.price;
      if (chgEl) {
        chgEl.textContent  = val.chg;
        chgEl.className    = 'stk-c ' + (val.up ? 'up' : 'dn');
      }
    }
  } catch(e) {
    console.log('Stock fetch error:', e);
  }
}

// Load stocks on page load, refresh every 5 minutes
if (document.getElementById('stocks-box')) {
  loadStocks();
  setInterval(loadStocks, 5 * 60 * 1000);
}
