(function ($) {
    "use strict";
    
    // Initiate the wowjs animation library
    new WOW().init();

    // Initiate nav menu
    $('.menu, .overlay').click(function () {
        $('.menu').toggleClass('clicked');
        $('#nav').toggleClass('show');
    });
    
    //Portfolio modal slider
    $('.port-slider').slick({
        autoplay: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.port-slider-nav'
    });
    $('.port-slider-nav').slick({
        autoplay: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.port-slider',
        arrows: false,
        dots: false,
        centerMode: true,
        focusOnSelect: true
    });
    
    $('#popover-content-download').hide();
    $("[data-toggle=popover]").each(function (e) {
        $(this).popover({
            html: true,
            content: function () {
                var id = $(this).attr('id')
                return $('#popover-content-' + id).html();
            }
        });

    });
	
	// Date and time picker of booking section
    $('#date-1, #date-2').datetimepicker({
        format: 'L'
    });
    $('#time-1, #time-2').datetimepicker({
        format: 'LT'
    });
})(jQuery);

