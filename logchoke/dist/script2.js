
$(".answer").hide();
$(".coupon_question").click(function() {
    if($(this).is(":checked")) {
        $(".answer").show();
    } else {
        $(".answer").hide();
    }
});

//character names;

  function EnterNames() {
    var p = document.getElementById('your_paragraph');
    var btn = document.getElementById('btnEnterNames');

// add more here
// Part 1
    var s =
    document.getElementsByClassName('tmetme');
    var sname = document.getElementById('box-tmetme').value;
    if (sname == '') sname = 'tmetme';
    for (i = 0; i < s.length; i++) {
        s[i].textContent = sname;
    }

    var l =
    document.getElementsByClassName('location');
    var lname = document.getElementById('box-location').value;
    if (lname == '') lname = 'location';
    for (i = 0; i < l.length; i++) {
        l[i].textContent = lname;
    }

    var s =
    document.getElementsByClassName('breefomeet');
    var sname = document.getElementById('box-breefomeet').value;
    if (sname == '') sname = 'breefomeet';
    for (i = 0; i < s.length; i++) {
        s[i].textContent = sname;
    }

    var l =
    document.getElementsByClassName('leader');
    var sname = document.getElementById('box-leader').value;
    if (sname == '') sname = 'leader';
    for (i = 0; i < l.length; i++) {
        l[i].textContent = sname;
    }    

    var t =
    document.getElementsByClassName('topic');
    var tname = document.getElementById('box-topic').value;
    if (tname == '') tname = 'topic';
    for (i = 0; i < t.length; i++) {
        t[i].textContent = tname;
    }   

// Part 2
    var k =
    document.getElementsByClassName('machine');
    var kname = document.getElementById('box-machine').value;
    if (kname == '') kname = 'machine';
    for (i = 0; i < k.length; i++) {
        k[i].textContent = kname;
    }   
    
    var o =
    document.getElementsByClassName('model');
    var oname = document.getElementById('box-model').value;
    if (oname == '') oname = 'model';
    for (i = 0; i < o.length; i++) {
        o[i].textContent = oname;
    }       

    var c =
    document.getElementsByClassName('check1');
    var cname = document.getElementById('box-check1').value;
    if (cname == '') cname = 'check1';
    for (i = 0; i < c.length; i++) {
        c[i].textContent = cname;
    }       

    var k =
    document.getElementsByClassName('check2');
    var kname = document.getElementById('box-check2').value;
    if (kname == '') kname = 'check2';
    for (i = 0; i < k.length; i++) {
        k[i].textContent = kname;
    }     
  

// stop adding more!
  
};
