$(document).ready(function(){
	$(".tshirtimg").hover(function(){
    //$(this).css("background-color", "yellow");
    	$(this).find(".btnelement").show();
    }, function(){
    	$(this).find(".btnelement").hide();
  	});
	$(".btnelement").hover(function(){
		$(this).css({"background-color":"white","color":"black"});
	},function(){
		$(this).css({"background-color":"rgba(0,0,0,0.5)","color":"white"});
	});
	$(".backbtn").hover(function(){
      $(".bchtext").show();
    },function(){
      $(".bchtext").hide();
    });
    // $(".backbtn").click(function(){
    //    window.location.href="{% url 'men_items' %}";
    // });
});