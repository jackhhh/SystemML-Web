(function(window) {
    "use strict";

    var set_algorithm_menu_highlight = function(algorithm) {
        var sidebar = $("#sidebar-menu");
        var item = sidebar.find("." + algorithm);
        $(".active").removeClass("active");
        if(item.length > 0) {
            item = item[0];
            $(item).addClass("active");
            var parent = item.parentElement;
            while(parent && !$(parent).hasClass("treeview")) {
                if(parent.tagName.toLowerCase() === "ul") {
                    parent.style.display = "block";
                }
                parent = parent.parentElement;
            }
            $(parent).addClass("menu-open");
            $(parent).addClass("active");
        }
    };

    var load = function() {
        if(window.algorithm_name) {
            set_algorithm_menu_highlight(window.algorithm_name);
        }
    };

    window.addEventListener("load", load, false);
})(window);

function submit(){
    var info = document.getElementsByClassName('form-control');

}