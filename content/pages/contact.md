title: Contact

<div style="text-align: center;">
<a href="https://instagram.com/downrightdad" style="text-decoration: none !important;border-bottom:none;" target="_blank"><i class="fab fa-instagram fa-2x" style="text-decoration: none !important" ></i></a>
<a href="https://twitter.com/downrightdad" style="text-decoration: none !important;border-bottom:none;" target="_blank"><i class="fab fa-twitter fa-2x" style="text-decoration: none !important"></i></a>
</div>

If you'd like to get in touch with me, check me out on [Twitter](https://twitter.com/downrightdad) or [Instagram](https://instagram.com/downrightdad) or shoot me a message:


<style>
body {font-family: Arial, Helvetica, sans-serif;}


input[type=text],input[type=email], textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<!--
<div class="container">
  <form action="#">
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email..">
    <label for="subject">Subject</label>
    <textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>
    <input type="submit" value="Submit">
  </form>
</div>
-->

<div class="container">

<form name="contact" method="POST" data-netlify="true">
  <p>
    <label>Your Name: <input type="text" name="name" /></label>   
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" /></label>
  </p>
  <p>
    <label>Message: <textarea name="message"></textarea></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
</div>