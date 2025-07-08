// Update slider value text
const slider = document.getElementById('remote_slider');
const sliderText = document.getElementById('slider_value');

if (slider && sliderText) {
  slider.addEventListener('input', () => {
    sliderText.textContent = slider.value;
  });
}
