DUMMY CSV FILE
0-dummy.csv
Jo Doe,jo@doe.com,465785
Joa Doe,joa@doe.com,123456
Job Doe,job@doe.com,234567
Joe Doe,joe@doe.com,345678
Jog Doe,jog@doe.com,578456
Joh Doe,joh@doe.com,378945
Joi Doe,joi@doe.com,456789
Jon Doe,jon@doe.com,987654
Jor Doe,jor@doe.com,754642
Joy Doe,joy@doe.com,124578
Let us start with a dummy CSV file, a list of dummy users. For the folks who are new to “comma separated values”:

CSV files are just plain text.
We use line breaks \r\n to indicate rows.
We use commas , to indicate columns.
If the cell contains a comma, the value will be enclosed in quotes. E.g. "Joy, Doe"
 


 

EXAMPLE 1) CSV FILE PICKER TO HTML TABLE
1A) THE HTML
1a-read-csv.html
<!-- (A) PICK CSV FILE -->
<input type="file" accept=".csv" id="demoPick">
 
<!-- (B) GENERATE HTML TABLE HERE -->
<table id="demoTable"></table>
<input type="file"> A file picker… Restricted to CSV files only.
<table id="demoTable"> Empty table to show the CSV contents.
 

1B) THE JAVASCRIPT
1b-read-csv.js
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
That is quite a bit of Javascript code, but here is a quick summary.

reader = new FileReader() We will use this file reader object to read the selected CSV file.
reader.readAsText() When the user picks a CSV file, we will read it as plain text.
When reader is done reading the selected CSV file.
rows = reader.result.split("\r\n") Split the raw data into rows by the line breaks.
cols = row.match(/(?:\"([^\"]*(?:\"\"[^\"]*)*)\")|([^\",]+)/g) Further break each row into columns.
tr = table.insertRow() and td = tr.insertCell() Self-explanatory… Add the rows and columns to the HTML table.
 

EXAMPLE 2) AJAX READ CSV FILE
2A) THE HTML
2a-ajax-csv.html
<!-- (A) GENERATE HTML TABLE HERE -->
<table id="demoTable"></table>
For this example, we only need an empty table.

 


 

2B) THE JAVASCRIPT
2b-ajax-csv.js
// (A) GET HTML TABLE
let table = document.getElementById("demoTable");

// (B) AJAX FETCH CSV FILE
fetch("0-dummy.csv")
.then(res => res.text())
.then(csv => {
  // (B1) REMOVE OLD TABLE ROWS
  table.innerHTML = "";

  // (B2) GENERATE TABLE
  let rows = csv.split("\r\n");
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
});
Look no further, this is pretty much the same.

fetch("0-dummy.csv") Gets the CSV file on the server.
.then(res => res.text()) Reads the CSV as plain text.
.then(csv => { ... }) Pretty much the same as above. Break the string down into rows/columns, and generate the HTML table.
 

EXTRA BITS & LINKS

That’s all for this project, and here is a small section on some extras that may be useful to you.

 

A NOTE ABOUT THE PERFORMANCE
As you can see, we are reading an entire CSV file into a string. This works, but you will run into performance issues and “out of memory” problems with massive CSV files. At the time of writing, there are no ways to read a CSV file line-by-line… At least in client-side Javascript. So just be aware of this, and work with it carefully.

P.S. If you are using the file picker, you can get the selected file size with picker.files[0].size.

 
