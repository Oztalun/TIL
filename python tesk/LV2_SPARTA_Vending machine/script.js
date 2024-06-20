// script.js
document.addEventListener('DOMContentLoaded', function () {
    let selectedProduct = null;
    const products = document.querySelectorAll('.product button');
    const buyButton = document.getElementById('buy-button');
    const moneyInput = document.getElementById('money');
    const messageDiv = document.querySelector('.message');

    products.forEach(button => {
        button.addEventListener('click', function () {
            const product = this.parentElement;
            selectedProduct = {
                name: product.querySelector('span').innerText,
                price: parseInt(product.dataset.price)
            };
            messageDiv.textContent = `${selectedProduct.name} 선택됨. 가격: ${selectedProduct.price}원`;
            messageDiv.style.color = 'black';
        });
    });

    buyButton.addEventListener('click', function () {
        const money = parseInt(moneyInput.value);
        if (!selectedProduct) {
            messageDiv.textContent = '제품을 선택하세요.';
            messageDiv.style.color = 'red';
            return;
        }

        if (isNaN(money) || money < selectedProduct.price) {
            messageDiv.textContent = '금액이 부족합니다.';
            messageDiv.style.color = 'red';
            return;
        }

        messageDiv.textContent = `${selectedProduct.name}을(를) 구매했습니다. 거스름돈: ${money - selectedProduct.price}원`;
        messageDiv.style.color = 'green';
        selectedProduct = null;
        moneyInput.value = '';
    });
});
