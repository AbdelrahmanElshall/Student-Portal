
let upNav = $('.upper-navbar').innerHeight(),
    navH  = $('.navbar').innerHeight(),
    winH  = $(window).height();

$('.slider,.carousel-item').height(winH-(upNav+navH));

$(window).on('resize',function() {
    let upNav = $('.upper-navbar').innerHeight(),
        navH  = $('.navbar').innerHeight(),
        winH  = $(window).height();
    $('.slider,.carousel-item').height(winH-(upNav+navH));

});

/*Start of the shuffle*/

$(function() {

    $('.features ul > li').on('click',function(){
        $(this).addClass('active').siblings().removeClass('active')
        console.log($(this).data('class'));
        if($(this).data('class')=="all"){
            $(".features-work .row .col-md").css('opacity',1)
        }
        else{
            $(".features-work .row .col-md").css('opacity',"0.09")
            $($(this).data('class')).parent().css('opacity',1)
        }
        
    });
    
});
/*end of shuffle*/



/* start of search bar*/


function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}


/* end of search bar*/