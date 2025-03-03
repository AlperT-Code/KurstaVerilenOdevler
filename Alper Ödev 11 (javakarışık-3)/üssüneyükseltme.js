let sayi = parseFloat(prompt("Bir sayı girin:"));
let us = parseInt(prompt("Bir üs girin:"));

let sonuc = 1;
let i = 0;

while (i < us) {
    sonuc *= sayi;
    i++;
}

alert(`${sayi} sayısının ${us} üssü: ${sonuc}`);