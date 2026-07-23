Analyze the access log file and create /app/report.json.

The report.json file must be valid JSON and contain:

1. A total_requests field containing the total number of requests in /app/access.log.

2. A unique_ips field containing the number of unique IP addresses found in /app/access.log.

3. A top_path field containing the most frequently requested URL path.

4. The generated file must be written to the exact location /app/report.json.