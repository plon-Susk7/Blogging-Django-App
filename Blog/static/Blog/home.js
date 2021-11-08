
function getAllPost(){
    
    fetch('/posts')
    .then(response=>response.json())
    .then(data=>{
        const Div = document.createElement('div');
        Div.className = "body-item";
        data.forEach(function(obj){
            Div.innerHTML+= `
            <div class="blog-posts border border-light">
            <h3>${obj.title}</h3>
            <br>
            <img src="${obj.image}" style="object-fit:cover;width:100%;height:250px;"></img>
            <br>
            <h5>${obj.description}</h5>
            <br>
            <a href="/blogpost/${obj.id}">Read More...</a>
            <br>
            <h6>-${obj.author}</h6>
            <br>
            <h6>${obj.timestamp}<h6>
            <div>`
            
        })
        document.querySelector('.body').appendChild(Div)
    })
}

window.onload = getAllPost();