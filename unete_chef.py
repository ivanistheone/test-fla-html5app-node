#!/usr/bin/env python

from ricecooker.chefs import SushiChef
from ricecooker.classes import licenses
from ricecooker.classes.files import HTMLZipFile, ThumbnailFile
from ricecooker.classes.nodes import ChannelNode, HTML5AppNode, TopicNode
from ricecooker.utils.zip import create_predictable_zip


TEST_FLASH_DIR = './chefdata/flash_test_zip_dir'
TEST2_FLASH_DIR = './chefdata/flash_test2_zip_dir'

class UneteTestChef(SushiChef):
    """
    This is my sushi chef...
    """
    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'unete.org',       # make sure to change this when testing
        'CHANNEL_SOURCE_ID': 'test-flash-preliminary',   # channel's unique id
        'CHANNEL_TITLE': 'A test channel with flash content as a',
        #'CHANNEL_THUMBNAIL': 'http://yourdomain.org/img/logo.jpg', # (optional) local path or url to image file
        #'CHANNEL_DESCRIPTION': 'What is this channel about?',      # (optional) description of the channel (optional)
    }

    def construct_channel(self, **kwargs):
        channel = self.get_channel(**kwargs)
        potato_topic = TopicNode(source_id="<potatos_id>", title="Potatoes!")
        channel.add_child(potato_topic)

        # THIS ONE DOESN'T WORK
        # zippath = create_predictable_zip(TEST_FLASH_DIR)
        # print('>>>>> created zip file here', zippath)
        # html5app = HTML5AppNode(
        #     files=[HTMLZipFile(zippath)],
        #     title='Test flash HTML5 app',
        #     source_id='test_flash_obj',
        #     license=licenses.PublicDomainLicense(),
        # )
        # potato_topic.add_child(html5app)

        zippath = create_predictable_zip(TEST2_FLASH_DIR)
        print('>>>>> created zip file here', zippath)
        html5app = HTML5AppNode(
            files=[HTMLZipFile(zippath)],
            title='Second Test flash HTML5 app',
            source_id='test2_flash_obj',
            license=licenses.PublicDomainLicense(),
        )
        potato_topic.add_child(html5app)

        return channel



if __name__ == '__main__':
    chef = UneteTestChef()
    chef.main()

