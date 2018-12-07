const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  const coords = data.split('\n').map(
    (str) => [
      ...str.split(',').map(
        (xy) => parseInt(xy.trim(), 10)
      ) ]); coords.pop(); main(coords); });

function main(coords) {
  const ext = getExtremities(coords);
  const counting = [];

  for (let x = ext.xMin + 1; x < ext.xMax; x++) {
    for (let y = ext.yMin + 1; y < ext.yMax; y++) {
      closest = getClosestCoord([x, y], coords);
      if (!counting[closest]) {
        counting[closest] = 1;
      }
      counting[closest] += 1;
    }
  }

  console.log(counting);
  const max = Math.max(...counting);
  const indexy = counting.findIndex((score) => score === max)
  console.log(max, indexy);
  console.log(coords[indexy]);
}

function manhattan(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function getClosestCoord(loc, coords) {
  lowest = [];
  scores = coords.map((coord) => manhattan(loc, coord));
  scores.forEach((score, i) => {
    if(score === lowest[0]) {
      lowest.push([score, i]);
    } else if(!lowest.length || score < lowest[0][0]) {
      lowest = [[score, i]];
    }
  });

  if (lowest.length > 1) {
    return null;
  }

  return lowest[0][1];
}

function getExtremities(coords) {
  const xMax = coords
    .reduce((a, c) => c[0] > a || a === null ? c[0] : a, null);
    
  const xMin = coords
    .reduce((a, c) => c[0] < a || a === null ? c[0] : a, null);

  const yMax = coords
    .reduce((a, c) => c[1] > a || a === null ? c[1] : a, null);

  const yMin = coords
    .reduce((a, c) => c[1] < a || a === null ? c[1] : a, null);

  return {
    xMax: xMax,
    xMin: xMin,
    yMax: yMax,
    yMin: yMin,
  };
}
