let products = document.getElementsByClassName('add-to-cart-btn')



let element = 0
for (;element < products.length;) {
    products[element].id = 'item'+element
    element++
}
function AddToCart(){
    let clicked_btn = document.getElementById(event.target.id)
    let parent = clicked_btn.parentElement.parentElement;
    selected_item_details = {
        product_img: parent.childNodes[7].childNodes[1].src,
        product_name: parent.childNodes[1].innerText,
        product_price: parent.childNodes[5].childNodes[0].innerText
    }
    localStorage.setItem(`${clicked_btn.id}`, JSON.stringify( selected_item_details))
    let b = parseInt(basket_quantity.innerText)
    b ++
    basket_quantity.innerText = b
    basket_quantity.value = b
    // console.log(clicked_btn.id);
}
let basket_quantity = document.getElementById('no-of-basket-items');
basket_quantity.innerText = localStorage.length


