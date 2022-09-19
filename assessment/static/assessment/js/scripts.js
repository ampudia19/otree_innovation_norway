// Scroll to the top on tab change
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// Automatic check boxes
function check_boxes(checked=true, array_input=null) {
  const parsed_array = array_input.map(function(item) {
    return 'input[name=\"' + item + '\"]';
  }).join(", ")
  const checkboxes = document.querySelectorAll(parsed_array)
  checkboxes.forEach((checkbox) => {
    checkbox.checked = checked;
  });
}

// Smooth scrolling
jQuery(document).ready(function($) {
	
  $('.functionforscroll').on('click',function (e) {
  e.preventDefault();
  var target = "#" + $(this).text(),
  $target = $(target);
  $('html, body').stop().animate({
      'scrollTop': $target.offset().top-90
  }, 400, 'swing');
 });
});

// Show and hide dynamically
function showDiv(id) {
  document.getElementById(id).style.display = "block";
}
function hideDiv(id) {
  document.getElementById(id).style.display = "none";
}

// Real-time sums
$(document).ready(function(){
  $(".cost").on("input",function() {
    var total=0;
    $("[id*='_offered']") .each(function(){
      if(!isNaN(parseInt($(this).val())))
      {
        total+=parseInt($(this).val());  
      }
    });
    $(".cost-total").val(total);
    });
  })

$(document).ready(function(){
  fitt = $(".in-sugg").text()
  $(".in-offer").on("input",function() {
    $("[id*='INfund_finoffered']").each(function(){
      if(!isNaN(parseInt($(this).val())))
      {
        total=(parseFloat(parseInt($(this).val(), 10) * 100) / parseFloat(fitt)).toFixed(2);  
      }
    });
    $(".in-perc").val(total);
    });
  })

$(document).ready(function(){
  fitt2 = $(".af-sugg").text()
  $(".af-offer").on("input",function() {
    $("[id*='AFfund_finoffered']").each(function(){
      if(!isNaN(parseInt($(this).val())))
      {
        total=(parseFloat(parseInt($(this).val(), 10) * 100) / parseFloat(fitt2)).toFixed(2);  
      }
    });
    $(".af-perc").val(total);
    });
  })

  $(document).ready(function(){
    $(".finoffer").on("input",function() {
      var total=0;
      $("[id*='_finoffered']") .each(function(){
        if(!isNaN(parseInt($(this).val())))
        {
          total+=parseInt($(this).val());  
        }
      });
      $(".fin-total").val(total);
      });
    })