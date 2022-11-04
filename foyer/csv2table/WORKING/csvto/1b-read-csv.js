// (A) FILE READER + HTML ELEMENTS
let reader = new FileReader(),
    picker = document.getElementById("demoPick"),
    table = document.getElementById("demoTable");

// (B) READ CSV ON FILE PICK
picker.onchange = () => reader.readAsText(picker.files[0]);

// (C) READ CSV & GENERATE TABLE
// CREDIT : https://thegermancoder.com/2018/11/29/how-to-parse-csv-with-javascript/
reader.onloadend = () => {
  table.innerHTML = "";
  let rows = reader.result.split("\r\n");
  for (let row of rows) {
    let cols = row.match(/(?:\"([^\"]*(?:\"\"[^\"]*)*)\")|([^\",]+)/g);
    if (cols!=null) {
      let tr = table.insertRow();
      for (let col of cols) {
        let td = tr.insertCell();
        td.innerHTML = col.replace(/(^"|"$)/g, "");
      }
    }
  }
};