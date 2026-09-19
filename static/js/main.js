document.addEventListener('DOMContentLoaded', () => {
  const cards = [...document.querySelectorAll('.question-card')];
  const form = document.querySelector('#quiz-form');
  if (cards.length && form) {
    let current = 0;
    const next = document.querySelector('#next');
    const previous = document.querySelector('#previous');
    const submit = document.querySelector('#submit');
    const label = document.querySelector('#progress-label');
    const bar = document.querySelector('#progress-bar');
    const render = () => {
      cards.forEach((card, index) => { card.hidden = index !== current; });
      label.textContent = `Question ${current + 1} of ${cards.length}`;
      bar.style.width = `${((current + 1) / cards.length) * 100}%`;
      previous.disabled = current === 0;
      next.hidden = current === cards.length - 1;
      submit.hidden = current !== cards.length - 1;
    };
    next.addEventListener('click', () => { current = Math.min(current + 1, cards.length - 1); render(); });
    previous.addEventListener('click', () => { current = Math.max(current - 1, 0); render(); });
    form.addEventListener('submit', (event) => { if (!window.confirm('Submit this test and calculate your score?')) event.preventDefault(); });
    render();
    const timer = document.querySelector('#timer');
    let seconds = Number(timer.dataset.duration);
    const tick = () => { const minutes = Math.floor(seconds / 60); const remaining = seconds % 60; timer.textContent = `${String(minutes).padStart(2, '0')}:${String(remaining).padStart(2, '0')}`; if (seconds <= 0) form.submit(); else seconds -= 1; };
    tick();
    setInterval(tick, 1000);
  }
});
