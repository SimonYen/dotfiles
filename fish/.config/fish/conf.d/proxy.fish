function proxyon
	set -gx http_proxy http://localhost:7890
	set -gx https_proxy http://localhost:7890
end

function proxyoff
	set -e http_proxy
	set -e https_proxy
end
	
