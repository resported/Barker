$(document).ready(function () {
    $('.men-dropdown').hide();
    $('.woman-dropdown').hide();
    $('.ul-size li').hide();

    $('.woman').hover(function () {
        $('.woman-dropdown').show();
    },
    function () {
        $('.woman-dropdown').hide();
        })

    $('.men').hover(function () {
        $('.men-dropdown').show();
    },
    function () {
        $('.men-dropdown').hide();
    })
});
