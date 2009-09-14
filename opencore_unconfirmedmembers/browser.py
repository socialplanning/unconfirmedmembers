from opencore.browser.base import BaseView
from opencore.browser.formhandler import OctopoLite, action
from opencore.member.interfaces import IHandleMemberWorkflow as IWorkflowed
from Products.CMFCore.utils import getToolByName as get_tool
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile as Template

class UnconfirmedMembers(BaseView, OctopoLite):

    template = Template('template.pt')

    def list(self):
        members = get_tool(self.context, 'membrane_tool'
                           ).unrestrictedSearchResults(
            review_state=['new','pending'])

        return members
    
    @action('confirm')
    def confirm(self, targets, fields):
        members = get_tool(self.context, 'portal_memberdata')

        result = []

        for id in targets:
            member = IWorkflowed(members[id])
            if member.is_unconfirmed:
                member.confirm()

                result.append(id)

        ### XXX TODO i18n
        self.add_status_message('confirmed %d accounts' % len(result))
        return self.redirect(self.context.absolute_url() + '/review_members')

    #@action('delete')
    #def delete(self, targets, fields):
    #    pass

    #@action('remind')
    #def remind(self, targets, fields):
    #    pass
