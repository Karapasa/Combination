function removeRow (btn)
{
var ro = btn.parentNode.parentNode;
var ta = document.getElementById ('tbl')
ta.deleteRow (ro.rowIndex);
if (ta.rows.length == 1) ta.getElementsByTagName ('input') [1].disabled = 1;
}

function addRow ()
{
var ta = document.getElementById ('tbl');
var ro = ta.rows [ta.rows.length - 1];
var num = parseInt (ro.getElementsByTagName ('input') [0].name.substr (1)) + 1;
newro = ro.cloneNode (1);
newro.getElementsByTagName ('input') [0].name = 'n' + num;
   ro.getElementsByTagName ('input') [1].disabled =
newro.getElementsByTagName ('input') [1].disabled = 0;
ta.appendChild (newro);
}