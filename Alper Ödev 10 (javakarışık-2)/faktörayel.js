let sayi = prompt("Lütfen bir pozitif tam sayı girin:");
sayi = parseInt(sayi);

let faktörayel = 1;
let i = 1;

while (i <= (sayi >= 0 ? sayi : 0)) {
    faktörayel *= i;
    i++;
}

alert(`${sayi} sayısının faktöriyeli: ${faktörayel}`);