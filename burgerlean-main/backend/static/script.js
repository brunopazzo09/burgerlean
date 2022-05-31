var cart=[];

function addToCart(burgerID){
    cart.push(burgerID);

    for(let i=0;i<cart.length;i++)
        console.log("Carrello: "+cart[i]);
}