# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/opcit
# catalog-date 2006-09-21 21:56:41 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-opcit
Version:	1.1
Release:	5
Summary:	Footnote-style bibliographical references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/opcit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package addresses the problem of expressing citations in a
style that is natural for humanities studies, yet does not
interfere with the flow of text (as author-year styles do). The
package differs from footbib in that it uses real footnotes,
potentially in the same series as any of the document's other
footnotes. Opcit also, as its name implies, avoids repetition
of full citations, achieving this, to a large extent,
automatically.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/opcit/opcit.bst
%{_texmfdistdir}/tex/latex/opcit/opcit.sty
%doc %{_texmfdistdir}/doc/latex/opcit/README
%doc %{_texmfdistdir}/doc/latex/opcit/opcit.pdf
#- source
%doc %{_texmfdistdir}/source/latex/opcit/opcit.dtx
%doc %{_texmfdistdir}/source/latex/opcit/opcit.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 754551
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719164
- texlive-opcit
- texlive-opcit
- texlive-opcit
- texlive-opcit

