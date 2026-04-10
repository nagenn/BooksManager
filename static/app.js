
console.log("Book manager loaded")

async function loadBooks(){
const r = await fetch("/api/books")
const data = await r.json()
console.log(data)
}

loadBooks()
