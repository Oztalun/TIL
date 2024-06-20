document.addEventListener('DOMContentLoaded', function () {
    const submitElem = document.getElementById('submit');
    const chancesElem = document.getElementById('chances');
    const usedAlphabetsElem = document.getElementById('used-alphabets');
    const guessInput = document.getElementById('guess-input');
    const guessButton = document.getElementById('guess-button');
    const messageElem = document.getElementById('message');

    function updateGame(data) {
        submitElem.textContent = data.submit.split('').join(' '); // 밑줄 사이에 공간 추가
        chancesElem.textContent = data.chances;
        usedAlphabetsElem.textContent = data.used_alphabets.join(', ');
        messageElem.textContent = data.message;

        if (data.game_over) {
            guessButton.disabled = true;
            guessInput.disabled = true;
            messageElem.textContent += ' 게임이 끝났습니다!';
        }
    }

    guessButton.addEventListener('click', function () {
        const guess = guessInput.value.toLowerCase();
        if (guess.length === 1 && /^[a-z]$/.test(guess)) {
            fetch('/guess', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ guess: guess })
            })
            .then(response => response.json())
            .then(data => updateGame(data))
            .catch(error => console.error('Error:', error));
        } else {
            messageElem.textContent = '영어 한 글자를 입력하세요.';
        }
        guessInput.value = '';
    });

    // 초기 게임 상태 로드
    fetch('/')
    .then(response => response.text())
    .then(() => {
        submitElem.textContent = 'Loading...';
        chancesElem.textContent = 'Loading...';
        usedAlphabetsElem.textContent = 'Loading...';
    })
    .catch(error => console.error('Error:', error));
});
