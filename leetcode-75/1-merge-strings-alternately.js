/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  let newString = ''

  let length = word1.length > word2.length ? word1.length : word2.length

  for (let i = 0; i < length; i++) {
    if (word1[i]) {
      newString += word1[i]
    }
    if (word2[i]) {
      newString += word2[i]
    }
  }

  return newString
}

console.log(mergeAlternately('java', 'script'))
