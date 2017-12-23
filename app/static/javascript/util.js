function toTitleCase(str) {
  return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

function alphabetize(data) {
  data.sort(function(a, b) {
    var splitA = a.name.split(" ");
    var splitB = b.name.split(" ");
    if(splitA[splitA.length-1] < splitB[splitB.length-1]) return -1;
    if(splitA[splitA.length-1] > splitB[splitB.length-1]) return 1;
    return 0;
  })
  return data;
}

function removeDuplicates(data) {
  var dict = {};
  var noDuplicates = [];
  // duplicates seem to occur when both http and https are available as URLs
  for (var i = 0; i < data.length; i++) {
    var urlSansProtocol = data[i].url.substring(data[i].url.indexOf("://") + 1);
    if (dict[urlSansProtocol] == undefined) {
      dict[urlSansProtocol] = data[i];
    } else {
      // prioritize https
      if (data[i].url.indexOf("https://") != -1) {
        var storedReview = dict[urlSansProtocol];
        dict[urlSansProtocol] = data[i];
        // have to keep review number consistent
        dict[urlSansProtocol]['review_num'] = storedReview['review_num'];
      }
    }
  }
  for (var key in dict) {
    noDuplicates.push(dict[key]);
  }
  return noDuplicates;
}

function flattenData(data) {
  var flattenedArray = [];
  data.forEach(function(datum, authorNum) {
    datum.nyt.forEach(function(d, reviewNum) {
      d['author_num'] = authorNum;
      d['review_num'] = reviewNum;
      flattenedArray.push(d);
    });
  });
  return flattenedArray;
}
