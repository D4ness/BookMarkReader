

let books_url = '/api/books';
let response = fetch(books_url);

let books = response.then((response) => {
    response.json().then((r)=>{
    for (const book of r){
    console.log(book)
        document.getElementById("bookList")
        .innerHTML+=`<li><a href="/${book.file_url}">${book.title}</a></li>`;

}
    console.log(r)
})
  }); // читаем ответ в формате JSON

// alert(books);


