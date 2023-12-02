curl "https://adventofcode.com/2023/day/$1/input" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-SG,en;q=0.9,zh-SG;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-Hans;q=0.4' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: session=53616c7465645f5fa0774b8e058501c8e18460f19f30332546b4f00e8f5b66fb5e2329c7d59ff9d6634a1076de534b112298582998007a11833320abb9b76a52' \
  -H 'dnt: 1' \
  -H 'referer: https://adventofcode.com/2023/day/1' \
  -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
  --compressed --output input.txt

mkdir -p $1
mv input.txt $1/input.txt
