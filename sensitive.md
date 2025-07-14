
- Username: donald.magoua95@gmail.com
- Password: Raspzero

- Host (THINGSBOARD_HOST_NAME): demo.thingsboard.io
- Token ($ACCESS_TOKEN): b16gFuQu0QNFSZ7iYgJP

- Device name: Raspberrypizero
- telemetry data path: v1/devices/me/telemetry

curl -v -X POST http://demo.thingsboard.io/api/v1/b16gFuQu0QNFSZ7iYgJP/telemetry --header Content-Type:application/json --data "{temperature:25}"