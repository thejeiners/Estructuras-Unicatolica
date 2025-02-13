const sbt = (a, b) => {
  let c = 0;
  while (b < a) {
    c++;
    b++;
  }

  return c;
};
console.log(sbt(2, 2));

const add = (a, b) => {
  let c = b;

  while (a > 0) {
    a--;
    c++;
  }
  return c;
};

console.log(add(5, 5));

const prod = (a, b) => {
  let c = 0;

  while (a > 0) {
    a--;
    c = c + b;
  }
  return c;
};

console.log(prod(6, 2));

const conc = (a, b) => {
  let c = 0;

  while (a >= b) {
    a = a - b;
    c++;
  }
  return c;
};

console.log(conc(7, 2));
