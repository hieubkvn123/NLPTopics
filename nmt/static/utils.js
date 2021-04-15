$(document).ready(function() {
	$("#translate-button").click(function() {
		// get the selected model
		var current_model = $("#model-selection").val()
		var current_text  = $("#input-text-area").val()
		var formData = new FormData()

		formData.append("model_name", current_model)
		formData.append("text", current_text)

		$.ajax({
			url : "/change_default_model",
			method : "POST",
			data : formData,
			async : true,
			contentType : false,
			processData : false,
			success : function(response) {
				if(response != 'fail') {
					$("#translated-text-area").val(response)
				}
			}
		})
	})
})
