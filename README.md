# TrophyMart - Backend

###### This is a basic flask application that calculates trophy prices.

### Usage:

Run wsgi.py and send get requests to http://localhost:5000/pricing/ with payload as JSON. Example payloads:

`{
	"shape": "cylinder",
	"height": "120",
	"radius": "25",
	"material": "steel",
	"coating": "gold"
}`

or
`
{
	"shape": "cuboid",
	"height": "120",
	"length": "25",
	"breadth": "50",
	"material": "steel",
	"coating": "silver"
}
`

The endpoint is highly configurable, reger to `app/config.py` for details.