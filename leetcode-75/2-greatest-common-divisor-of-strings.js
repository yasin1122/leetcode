var gcdOfStrings = function (str1, str2) {
  let big, small
  if (str1.length >= str2.length) {
    big = str1
    small = str2
  } else {
    big = str2
    small = str1
  }

  if (big.includes(small)) {
    return ''
  } else {
    findSmallestRepeatingPattern(small)
  }
}

function findSmallestRepeatingPattern(str) {
  // Loop through the string up to half its length to find the smallest repeating pattern
  for (let i = 1; i <= str.length / 2; i++) {
    // Check if the current length divides the string evenly
    if (str.length % i === 0) {
      // Extract the potential pattern
      const pattern = str.substring(0, i)
      let repeatedPattern = pattern.repeat(str.length / i)

      // Check if the constructed string matches the original string
      if (repeatedPattern === str) {
        return pattern // Return the repeating pattern
      }
    }
  }
  return str // Return the original string if no repeating pattern is found
}

console.log(gcdOfStrings('abababab', 'ababab'))
