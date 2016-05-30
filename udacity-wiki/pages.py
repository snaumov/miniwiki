__author__ = 'snaumov'

from flask import Blueprint, render_template, redirect, request

from forms import Page
from models import db, Pages, PageHistory
from app import app
from utilities import added_removed
import datetime
from sqlalchemy import and_

pages = Blueprint('pages', __name__)

@pages.route("/", methods=['GET', 'POST'])
def mainpage():
    form = Page()
    current_pages = db.session.query(Pages).all()
    return render_template('mainpage.html', form=form, current_pages=current_pages)

@pages.route("/<pagename>/edit", methods=['GET', 'POST'])
def editpage(pagename):
    page = db.session.query(Pages).filter(Pages.PageName==pagename).first()
    #pagehistory = db.session.query(PageHistory).filter(PageHistory.page_id==page.id).order_by(PageHistory.dateofchange.desc())
    form = Page(request.form)
    if page:
        if request.method == 'GET':
            form.PageContent.data = page.PageContent
            return render_template('pageedit.html', page=page, form=form)
        elif request.method == 'POST':
            content_added_removed = added_removed(page.PageContent, form.PageContent.data)
            newpagehistory = PageHistory(page_id=page.id, content_added=content_added_removed[0], content_removed=content_added_removed[1],
                                         currentcontent=form.PageContent.data, dateofchange=datetime.datetime.now())
            db.session.add(newpagehistory)
            db.session.commit()

            




            page.PageContent = form.PageContent.data
            app.logger.debug(form.PageContent.data)
            db.session.commit()
            return redirect('/%s' % pagename)

    else:
        pagename_capitalized = pagename.title() #to render a page header in Jinja
        if request.method == 'POST':
            newpage = Pages(PageName=pagename, PageContent=form.PageContent.data)
            db.session.add(newpage)
            db.session.commit()
            return redirect('/%s' % pagename)
        return render_template('pageedit_newpage.html', pagename=pagename_capitalized, form=form)

@pages.route("/<pagename>/history", methods=['GET'])
def historypage(pagename):
    page = db.session.query(Pages).filter(Pages.PageName==pagename).first()
    if page:
        pagehistory = db.session.query(PageHistory).filter(PageHistory.page_id==page.id).order_by(PageHistory.dateofchange.desc())
        return render_template('pagehistory.html', pagehistory=pagehistory, page=page)

@pages.route("/<pagename>/history/<id>", methods=['GET', 'POST'])
def hpage(pagename, id): #preview for one history of the page
    page = db.session.query(Pages).filter(Pages.PageName==pagename).first()

    ph = db.session.query(PageHistory).filter(and_(PageHistory.page_id==page.id, PageHistory.id == id)).first()
    app.logger.debug(ph.id)
    if (page is not None) & (ph is not None):
        if request.method == 'GET':
            return render_template('ph.html', ph=ph, pagename=pagename )
        elif request.method == 'POST':
            content_added_removed = added_removed(page.PageContent, ph.currentcontent)
            newpagehistory = PageHistory(page_id=page.id, content_added=content_added_removed[0], content_removed=content_added_removed[1],
                                         currentcontent=ph.currentcontent, dateofchange=datetime.datetime.now())
            db.session.add(newpagehistory)
            db.session.commit()






            page.PageContent = ph.currentcontent

            db.session.commit()
            return redirect('/%s' % pagename)

    else:
        return redirect('/<pagename>')

@pages.route("/<pagename>", methods=['GET'])
def page(pagename):
    page = db.session.query(Pages).filter(Pages.PageName==pagename).first()
    if page:
        return render_template('page.html', page=page)
    else:
        return redirect('/%s/edit' % pagename)
