$(document).ready(function(){
	$(".womentshirtpic").hover(function(){
    //$(this).css("background-color", "yellow");
    	$(this).find(".btnelement").show();
		$(this).css({"opacity":"0.3"});
    }, function(){
    	$(this).find(".btnelement").hide();
		$(this).css({"opacity":"1"});
	});
	$(".btnelement").hover(function(){
		$(this).css({"background-color":"white","color":"black"});
	},function(){
		$(this).css({"background-color":"black","color":"white"});
	});
	$(".backbtn").hover(function(){
      $(".bchtext").show();
    },function(){
      $(".bchtext").hide();
    });
	$(".addtocart").click(function(){
		var Product_Id=$(this).parent().parent().attr('id')
			$.ajax({
				type: 'post',
				url: "{% url 'addtocartajaxrequest' %}",
				data: {'Product_Id':Product_Id,'gender':'Women','person_category_id':'{{person_category_id}}'},  //JSON.stringify(obj)
				headers: {'X-CSRFToken': '{{ csrf_token }}'},
				async: true,
				success: function (response) {
					console.log(response);
					//id_='{{PersonId}}'
					//window.location.href = "http://127.0.0.1:8000/abcd?id="+id_+"";
				}
		   	}).done(function (data) {
				console.log(data);
			});	
	});
});