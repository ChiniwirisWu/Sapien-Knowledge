createPageForm = document.getElementById('create_page_form')

discardBtn = document.getElementById('discard-btn')
discardBtn.addEventListener('click', function(e){
		e.preventDefault()
		createPageForm.reset()
})
