#!/usr/bin/node

const request = require('request');
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlMovie, async function (error, response, body) {
  const arr = [];

  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      arr.push(myCharacter(film.characters[i]));
    }
  }

  let actors = await Promise.all(arr);

  actors = actors.map((actor) => JSON.parse(actor).name);
  actors.forEach((actor) => console.log(actor));
});

function myCharacter (thisCharacter) {
  return new Promise((resolve, reject) => {
    request(thisCharacter, function (error, response, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}
