$(document).ready(function(){
    new WOW().init();
    $('.header').height($(window).height());
    // $('#portfolio, #about, #contacts .header').height($(window).height());
    $(window).on('resize', function() {
        $('.header').height($(window).height());
        // $('#portfolio, #about, #contacts .header').height($(window).height());
    });
    $(".navbar a, .header button").click(function(){
    $("body,html").animate({
        scrollTop:$("#" + $(this).data('value')).offset().top
    },500)
 })
})