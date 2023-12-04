param(
    [string]$day
)

# Define the URL and headers
$url = "https://adventofcode.com/2023/day/$day/input"
$headers = @{
    'authority' = 'adventofcode.com'
    'accept' = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    'accept-language' = 'en-SG,en;q=0.9,zh-SG;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-Hans;q=0.4'
    'cache-control' = 'max-age=0'
    'cookie' = 'session=53616c7465645f5f66871e29fc1cd0c8ae45abfae27738019622aacb871f9c4b607000978f7f35a12d51be7f6593a0d921e4b6efcc33976dc75f143b4804772b'
    'dnt' = '1'
    'referer' = "https://adventofcode.com/2023/day/$day"
    'sec-ch-ua' = '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'
    'sec-ch-ua-mobile' = '?0'
    'sec-ch-ua-platform' = '"Linux"'
    'sec-fetch-dest' = 'document'
    'sec-fetch-mode' = 'navigate'
    'sec-fetch-site' = 'same-origin'
    'sec-fetch-user' = '?1'
    'upgrade-insecure-requests' = '1'
    'user-agent' = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# Make the request and save the output
$response = Invoke-WebRequest -Uri $url -Headers $headers
$outputFilePath = "$day\input.txt"

# Ensure the directory exists
$directory = Split-Path -Path $outputFilePath -Parent
if (-not (Test-Path -Path $directory)) {
    New-Item -ItemType Directory -Path $directory
}

# Write the response content to a file
$response.Content | Out-File $outputFilePath

