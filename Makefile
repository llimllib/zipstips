deploy:
	rsync -avuz . llimllib@hubvan.com:/srv/zipstips/ --exclude .git
	ssh llimllib@hubvan.com touch /srv/zipstips/wsgi.py
