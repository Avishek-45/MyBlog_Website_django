
document.addEventListener('DOMContentLoaded', function(event){ 
    console.log("This is a js page")
    let sc= document.createElement('srcipt')
    sc.setAttribute('src','https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');
    
    document.head.appendChild(sc);
    sc.onload = ()=>{
        tinymce.init({
        selector: '#id_content'
      });
    }
    
});