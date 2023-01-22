#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
