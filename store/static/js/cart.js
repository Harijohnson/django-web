

var updateBtns = document.getElementsByClassName('update-cart')

// console.log('outside user in variable : ',user)


for ( i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener("click",function(){
        var productId =this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('USER:', user)

        if (user=='AnonymousUser'){
            addCokieItem(productId, action) 
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}



function addCokieItem(productId, action){
    console.log('not loged in user')

    if (action=='add' )
    {
        if (cart[productId] === undefined)
        {
            cart[productId] = {'quantity':1}

        }
        else
        {
            cart[productId]['quantity'] += 1
        }
    }

    if (action =='remove' )
    {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0)
        {
            console.log('remove item')
            delete cart[productId]
        }
    }
   // console.log('Cart',cart)
    document.cookie = 'cart='+ JSON.stringify(cart) + ";domain;path=/"
   location.reload()
   console.log('Cart',cart)

}


















function updateUserOrder(productId,action){
    var url='/update_item/';
    fetch(url,{
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
       location.reload()
    });
}







// var shipping= document.getElementById('shipping')

// console.log('shipping true or false',shipping);


// if(shipping == 'False'){
//     document.getElementById('shipping-info').innerHTML ="";
// }

// if (user !== 'AnonymousUser'){
//     document.getElementById('user-info').innerHTML ="";
// }
// console.log('shipping :',shipping == 'False' )
// console.log('user here is :',user)


// if (shipping == 'False' &&  user !== 'AnonymousUser'){
// // hide the entire form if the user is loged in and shipping is false
// document.getElementById('form-wrapper').classList.add('hidden');
// // show payment if logged in user wants to buy an item that does not requires shipping
// document.getElementById('payment-info').classList.remove('hidden');
// }



// var form = document.getElementById('form')

// form.addEventListener('submit', function(e){
//     e.preventDefault()
//     console.log('form is submites')
//     document.getElementById('form-button').classList.add('hidden')
//     document.getElementById('payment-info').classList.remove('hidden')
// })
// document.getElementById('make-payment').addEventListener('click',function(e) {
//     submitFormData()
// })

// function submitFormData(){
//     console.log('payment button is clicked  ')
// }













