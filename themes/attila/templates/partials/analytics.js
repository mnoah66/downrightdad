

<script>
var host = window.location.hostname;
if(host != "localhost")
{
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-118771828-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '{{GOOGLE_ANALYTICS}}', { 'anonymize_ip': true });
    </script>

}
</script>
