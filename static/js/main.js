$(document).ready(function () {
    $('.woman-dropdown').hide();
    $('.men-dropdown').hide();
    $('.ul-size li').hide();

    $('.woman').hover(function () {
        $('.woman-dropdown').show(30);
    },
    function () {
        $('.woman-dropdown').slideUp(50);
        })

    $('.men').hover(function () {
        $('.men-dropdown').show(30);
    },
        function () {
            $('.men-dropdown').slideUp(50);
        })

})