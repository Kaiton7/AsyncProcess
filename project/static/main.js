// custom javascript

$(document).ready(() => {
  console.log('Sanity Check!');
  var oTable = $('#example').DataTable({
    'autoWidth': false,
    'serverSide': true,
    'processing': false,
    'responsive': true,
    'ajax': {
      'url': '/record/',
      'type': 'GET',
    }
  });
  console.log("finish ready in")
  setInterval(function () {
    oTable.ajax.reload();
  }, 1000);
});


// 
$('#DBGet').on('click', function () {
    console.log("dbget")
    $.ajax({
          url:'/dbget/',
          type:'GET',
      }).done(function (data) {
          console.log("dbget Succress")
          console.log(data)
      }).fail(function() {
         console.log("error")
      });
    });


//Download Resut CSV
$('#example').on('click', 'button', function () {
      var table = $('#example').DataTable();
      var datawt = table.row($(this).parents('tr')).data();
      $.ajax({
        url:'/DC/',
        type:'GET',
        data:{'fileid':datawt[0]},
    }).done(function (data) {
        console.log("dbget Succress");
        console.log(data);
        let downloadData = new Blob([data], {type: 'text/csv'});
  let filename = 'users.csv'
  
  // csv download 
  if (window.navigator.msSaveBlob) {
    window.navigator.msSaveBlob(downloadData, filename);
  } else {
    let downloadUrl  = (window.URL || window.webkitURL).createObjectURL(downloadData);
    let link = document.createElement('a');
    link.href = downloadUrl;
    link.download = filename;
    link.click();
    (window.URL || window.webkitURL).revokeObjectURL(downloadUrl);
  }
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log(jqXHR);
      console.log(textStatus);
      console.log(errorThrown);
      console.log("error get csv");
    });
 } );

// Insert Test Record
$('#WriteRecord').on('click', function () {
  $.ajax({
        url:'/recordwrite/',
        type:'GET',
    }).done(function (data) {
        console.log("dbget Succress")
        console.log(data)
    }).fail(function() {
       console.log("error")
    });
  });

//Show Table Record in console
$('#ShowDebug').on('click', function () {
    $.ajax({
          url:'/record/',
          type:'GET',
      }).done(function (data) {
          // 成功時の処理
          console.log("dbget Succress")
          console.log(data)
      }).fail(function() {
         // 失敗時の処理
         console.log("error")
      });
    });
  
  
// Kick Process
$('#Run').on('click', function () {
  console.log("execution")
  let $upfile = $('input[name="configfile"]');
let fd = new FormData();
fd.append("upfile", $upfile.prop('files')[0]);
$upfile.val('');

    $.ajax({
        url:'/tasks/file',
        type:'post',
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    }).done(function (data) {
        // 成功時の処理
        console.log(data)
    }).fail(function() {
       // 失敗時の処理
       console.log("error")
    });
  });
