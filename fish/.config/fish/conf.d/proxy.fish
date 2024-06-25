function proxyon
	set -gx HTTPS_PROXY http://localhost:7890
	set -gx HTTP_PROXY http://localhost:7890
	set -gx NO_PROXY localhost,127.0.0.1,.example.com
end

function proxyoff
	set -e HTTPS_PROXY
	set -e HTTP_PROXY
	set -e NO_PROXY
end
	
