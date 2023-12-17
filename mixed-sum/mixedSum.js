// function sumMix(x) {
//   let newArr = [];
//   x.map((e) => {
//     newArr.push(parseInt(e));
//   }),
//     console.log(newArr.reduce((acc, curr) => acc + curr, 0));
// }

// in one line just for fun
const sumMix = (x) => (x.reduce((acc, curr) => acc + parseInt(curr), 0));

// should return 22
sumMix([9, 3, "7", "3"]);
