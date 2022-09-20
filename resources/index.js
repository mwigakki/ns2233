function readTextFile(fileName) {
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", fileName, false);
  rawFile.onreadystatechange = function () {
    if (rawFile.readyState === 4) {
      if (rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        words = allText.split("\n"); // 0:title, 1:author, 2:paragraph1
        $(".read-title").text(words[0]);
        $(".read-content").text(words[2]);
      }
    }
  };
  rawFile.send(null);
}
window.onload = readTextFile("resources/dailyread.txt"); // 读取本地txt文件
