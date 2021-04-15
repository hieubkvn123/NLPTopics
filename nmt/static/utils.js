$(document).ready(function() {
	$("#translate-button").click(function() {
		// get the selected model
		var current_model = $("#model-selection").val()
		var formData = new FormData()
		formData.append("model_name", current_model)

		$.ajax({
			url : "/change_default_model",
			method : "POST",
			data : formData,
			async : true,
			contentType : false,
			processData : false,
			success : function(response) {
				console.log(response)
			}
		})
	})
})
